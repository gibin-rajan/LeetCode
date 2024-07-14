class Solution:
    def countOfAtoms(self, formula):
        # will contain hash-maps with count of elements in last meeted brackets
        n = len(formula)
        result_counter = {}
        parenthesis_stack = []
        cur_ind = 0

        while cur_ind < n:
            cur_char= formula[cur_ind]

            if cur_char == "(":
                cur_ind += 1
                parenthesis_stack.append({})
                continue

            if cur_char == ")":
                mult= ""
                cur_ind += 1

                while cur_ind < n and formula[cur_ind].isdigit():
                    mult += formula[cur_ind]
                    cur_ind += 1

                last_counter = parenthesis_stack.pop()
                target = parenthesis_stack[-1] if parenthesis_stack else result_counter
                for elem, counter in last_counter.items():
                    if elem not in target:
                        target[elem] = 0
                    target[elem] += counter * (int(mult) if mult else 1)
                continue

            cur_elem = ""
            cur_counter = ""
            target = parenthesis_stack[-1] if parenthesis_stack else result_counter

            while cur_ind < n and cur_char not in "()":
                if cur_char.isalpha():
                    if cur_char.isupper() and cur_elem != "":
                        if not cur_elem in target:
                            target[cur_elem] = 0
                        target[cur_elem] += int(cur_counter) if cur_counter else 1
                        cur_counter = ""
                        cur_elem = ""
                    cur_elem += cur_char
                else:
                    cur_counter += cur_char
                cur_ind += 1
                if cur_ind != n:
                    cur_char = formula[cur_ind]

            target = parenthesis_stack[-1] if parenthesis_stack else result_counter
            if not cur_elem in target:
                target[cur_elem] = 0
            target[cur_elem] += int(cur_counter) if cur_counter else 1

        parts= [
            elem + str(counter) if not counter == 1 else elem for elem, counter in result_counter.items()
        ]
        parts.sort()

        return "".join(parts)