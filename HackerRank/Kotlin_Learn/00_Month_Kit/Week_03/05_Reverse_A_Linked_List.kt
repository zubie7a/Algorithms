// https://www.hackerrank.com/challenges/one-month-preparation-kit-reverse-a-linked-list/problem

class SinglyLinkedListNode(nodeData: Int) {
    public var data: Int
    public var next: SinglyLinkedListNode?

    init {
        data = nodeData
        next = null
    }
}

class SinglyLinkedList {
    public var head: SinglyLinkedListNode?
    public var tail: SinglyLinkedListNode?

    init {
        head = null
        tail = null
    }

    public fun insertNode(nodeData: Int) {
        var node = SinglyLinkedListNode(nodeData)

        if (head == null) {
            head = node
        } else {
            tail?.next = node
        }

        tail = node
    }

}

fun printSinglyLinkedList(head: SinglyLinkedListNode?, sep: String) {
    var node = head;

    while (node != null) {
        print(node?.data)
        node = node?.next

        if (node != null) {
            print(sep)
        }
    }
}

/*
 * Complete the 'reverse' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     data: Int
 *     next: SinglyLinkedListNode
 * }
 *
 */

fun reverse(llist: SinglyLinkedListNode?): SinglyLinkedListNode? {
    // The initial node may be null meaning the list may be empty.
    var current = llist
    var prev: SinglyLinkedListNode? = null
    var next: SinglyLinkedListNode? = null
    while (current != null) {
        // Store the next element separately, 
        // e.g. (1) 2 3 4 5, next = 2
        next = current.next
        // At the current element, put as next the head of the
        // reversed chain which is stored at prev.
        current.next = prev
        // Now the head of the reversed chain is the current node.
        prev = current
        // And now the current node is the next in the original chain.
        current = next
    }
    
    return prev
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val tests = scan.nextLine().trim().toInt()

    for (testsItr in 1..tests) {
        val llistCount = scan.nextLine().trim().toInt()
        val llist = SinglyLinkedList()

        for (i in 0 until llistCount) {
            val llist_item = scan.nextLine().trim().toInt()
            llist.insertNode(llist_item)
        }

        val llist1 = reverse(llist?.head)

        printSinglyLinkedList(llist1, " ")
    }
}
