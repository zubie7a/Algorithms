# https://www.hackerrank.com/challenges/binary-search-tree-1
select n, 
    case
        # The parent is null.
        when p is null then "Root"
        # N is the parent of any node in the table.
        when n = any(select p from bst) then "Inner"
        else "Leaf"
    end
    from bst order by n
