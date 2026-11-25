import {createHash} from 'node:crypto';
import {execFile} from 'node:child_process';
import {createWriteStream} from 'node:fs';
import {access, lstat, mkdtemp, mkdir, rename, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {promisify} from 'node:util';
import {Readable, Transform} from 'node:stream';
import {pipeline} from 'node:stream/promises';
import {fileURLToPath} from 'node:url';

const archiveUrl = 'https://github.com/faidros/wastelandvastervik/releases/download/vastervik-city-2026-11-25/vastervik-ahmans-pack.tar.gz';
const expectedSha256 = 'c6ee126b0aebeb8be286af945885e8adf92523fdadc2baa6f7d90b6f71ba4faf';
const dist = fileURLToPath(new URL('../dist/', import.meta.url));
const city = join(dist, 'city');
const temp = await mkdtemp(join(tmpdir(), 'wasteland-city-'));
const stage = await mkdtemp(join(dist, '.city-staging-'));
const archive = join(temp, 'city.tar.gz');
const hash = createHash('sha256');

try {
  const response = await fetch(archiveUrl);
  if (!response.ok || !response.body) {
    throw new Error(`City pack download failed: HTTP ${response.status}`);
  }

  const hasher = new Transform({
    transform(chunk, encoding, callback) {
      hash.update(chunk);
      callback(null, chunk);
    },
  });
  await pipeline(Readable.fromWeb(response.body), hasher, createWriteStream(archive));

  const actualSha256 = hash.digest('hex');
  if (actualSha256 !== expectedSha256) {
    throw new Error(`City pack SHA-256 mismatch: expected ${expectedSha256}, got ${actualSha256}`);
  }

  await promisify(execFile)('tar', ['-xzf', archive, '-C', stage]);
  for (const file of ['config.json', 'map.json', 'tiles/tiles.json', 'tiles/base.glb']) {
    await access(join(stage, file));
  }

  try {
    const existing = await lstat(city);
    if (existing.isSymbolicLink()) {
      throw new Error(`Refusing to replace city symlink at ${city}`);
    }
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }

  await rm(city, {recursive: true, force: true});
  await rename(stage, city);
  console.log('Downloaded and verified the Västervik city pack.');
} finally {
  await rm(temp, {recursive: true, force: true});
  await rm(stage, {recursive: true, force: true});
}
