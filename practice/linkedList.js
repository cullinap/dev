// js linkedlist implementation

class listNode {
	constructor(data) {
		this.data = data
		this.next = null
	}
}

class linkedList {
	constructor(head = null) {
		this.head = head
	}

}

let node1 = new listNode(2);
let node2 = new listNode(5);

node1.next = node2;

let list = new linkedList(node1);

console.log(list.head.next.data)
