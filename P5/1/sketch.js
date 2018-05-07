
let v = 0;
let w = 10;
let ma;
let max;

function setup() {
  createCanvas(400, 400, WEBGL);
  ma = atan(cos(QUARTER_PI));
  max = dist(0, 0, 200, 200);
}

function draw() {
  background(100);
  ortho(-200, 200, 200, -200, 0, 1000);
  rotateX(-ma);
  rotateY(-QUARTER_PI)﻿

  for (let z = 0; z < height; z += w) {
    for (let x = 0; x < width; x += w) {
      push();
      let d = dist(x, z, width / 2, height / 2);
      let offset = map(d, 0, max, -PI, PI);
      let a = v + offset;
      let h = floor(map(sin(a), -1, 1, 100, 300));
      translate(x - width / 2, 0, z - height / 2);
      normalMaterial();
      box(w, h, w);
      //rect(x - width / 2 + w / 2, 0, w - 2, h);
      pop();
    }
  }

  v -= 0.1;
}
