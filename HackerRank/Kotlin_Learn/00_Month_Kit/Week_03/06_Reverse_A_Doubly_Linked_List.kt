// https://www.hackerrank.com/challenges/one-month-preparation-kit-reverse-a-doubly-linked-list/problem

class DoublyLinkedListNode(nodeData: Int) {
    public var data: Int
    public var next: DoublyLinkedListNode?
    public var prev: DoublyLinkedListNode?

    init {
        data = nodeData
        next = null
        prev = null
    }
}

class DoublyLinkedList {
    public var head: DoublyLinkedListNode?
    public var tail: DoublyLinkedListNode?

    init {
        head = null
        tail = null
    }

    public fun insertNode(nodeData: Int) {
        var node = DoublyLinkedListNode(nodeData)

        if (head == null) {
            head = node
        } else {
            tail?.next = node
            node?.prev = tail
        }

        tail = node
    }

}

fun printDoublyLinkedList(head: DoublyLinkedListNode?, sep: String) {
    var node = head;

    while (node != null) {
        print(node?.data)
        node = node?.next

        if (node != null) {
            print(sep)
        }
    }
}


// This is because the immutable test code is not printing a new
// line after a test case, which means the submission will be wrong.
var testCasesSoFar = 0

fun reverse(llist: DoublyLinkedListNode?): DoublyLinkedListNode? {
    var current = llist
    var temp: DoublyLinkedListNode? = null
    // This is similar to reversing the single linked list, but have
    // to consider that every node keeps two references, so we have to
    // update both of them.
    while (current != null) {
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    }
    
    // var copyPrev = prev
    // while (copyPrev != null) {
    //     println("cur: ${copyPrev?.data}, prev: ${copyPrev.prev?.data}, next: ${copyPrev.next?.data}")
    //     copyPrev = copyPrev.next
    // }
    if (testCasesSoFar > 0) {
        println()
    }
    testCasesSoFar++
    return temp?.prev
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val t = scan.nextLine().trim().toInt()

    for (tItr in 1..t) {
        val llistCount = scan.nextLine().trim().toInt()
        val llist = DoublyLinkedList()

        for (i in 0 until llistCount) {
            val llist_item = scan.nextLine().trim().toInt()
            llist.insertNode(llist_item)
        }

        val llist1 = reverse(llist?.head)

        printDoublyLinkedList(llist1, " ")
    }
}
