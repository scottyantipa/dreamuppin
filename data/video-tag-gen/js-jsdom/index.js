const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const frag = JSDOM.fragment(`<p>Hello</p><p><strong>Hi!</strong>`);
console.log('frag: ', frag);
console.log(frag.html());
