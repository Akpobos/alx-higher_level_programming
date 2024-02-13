#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        let x = "";
        for (let i = 0; i < this.width; i++) {
            x = x + "X";
        }

        for (let i = 0; i < this.height; i++) {
            console.log(x);
        }
    }
};

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

module.exports = Rectangle;
