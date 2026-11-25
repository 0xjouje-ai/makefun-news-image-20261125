// Entry program for "Sum up 25 November's world news in one image".
// The front page is drawn by draw.py (Pillow) and shipped as entry.png;
// this program copies that image to the output directory.
//
// Standard library only, no network. Runs twice with identical bytes.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

if (!existsSync(source)) {
  throw new Error("entry.png is missing next to main.ts");
}
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(source, dest);
console.log("wrote", dest, statSync(dest).size, "bytes");
