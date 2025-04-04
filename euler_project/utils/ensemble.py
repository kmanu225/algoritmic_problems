from time import time

def isPal(nbr):
    return str(nbr) == str(nbr)[::-1]

def sousEnsembles(L: list) ->list:
    # If the input list is empty, return a list containing only the empty set
    if len(L) == 0:
        return [L]

    else:
        ensemble = []  # Create an empty list to hold the subsets
        first_in = L[0]  # Get the first element of the list
        for anagramme in sousEnsembles(L[1::]):  # For each subset of the remaining elements
            # Add the subset to the list of subsets, both with and without the first element
            ensemble += [anagramme, [first_in] + anagramme]

    return ensemble  # Return the list of all subsets



def permutation_any(L: list) -> list:
    if len(L) <= 1:
        return [L]  # base case: return list with single element

    else:
        n = len(L)
        ensemble = []  # empty list to store permutations
        l = list(L)  # make a copy of the input list
        
        for i in range(n):
            # remove current element from copy of the list
            first_in = l.pop(i)
            
            # get all possible permutations of the remaining elements
            for anagramme in permutation_any(l):
                ensemble.append([first_in] + anagramme)  # add current element to each permutation
            
            # reset copy of the list
            l = list(L)
            
    return ensemble  # return list of all permutations




#Quicker
def combinaisons_backtrack(L: list, k: int) -> list:
    n = len(L)
    res = []

    # Backtracking function
    def backtrack(start: int, comb: list):
        # If we have found a combination of length k, append it to the result list and return
        if len(comb) == k:
            res.append(comb[:])  # Use [:] to append a copy of the list, not the original
            return

        # Iterate over the remaining elements of the list
        for i in range(start, n):
            comb.append(L[i])  # Add the current element to the combination
            backtrack(i + 1, comb)  # Recurse with the next element and the updated combination
            comb.pop()  # Remove the current element to backtrack and try the next one

    # Call the backtracking function with an empty combination and starting index of 0
    backtrack(0, [])

    return res


def combinaisons_all(ensemble: list, k: int):
    # Get the length of the list.
    n  = len(ensemble)

    # Set up the maximum value for i and j.
    i, i_max = 0, 2 ** n - 1
    j, j_max = 0, n - 1

    # Create an empty list to store the combinations.
    comb = []

    # Loop through all possible values of i.
    while i <= i_max:
        # Create an empty list to store the current combination.
        c = []
        # Check if the number of set bits in i is equal to k.
        if sum([int(i) for i in bin(i)[2::]]) == k:
            # Loop through all possible values of j.
            while j <= j_max:
                # Check if the jth bit of i is set.
                if (i >> j) & 1 == 1:
                    # If it is, add the corresponding element from the ensemble to the current combination.
                    c.append(ensemble[j])
                j += 1
            # Add the current combination to the list of combinations.
            comb.append(c)
            # Reset j to 0.
            j = 0
        # Increment i.
        i += 1

    # Return the list of combinations.
    return comb




if __name__ == "__main__":
    # k = 5
    # chiffres = [i for i in range(20)]
    start = time()
    # print(combinaisons_backtrack(chiffres, k))
    #print(combinaisons_all(chiffres, 2))
    mid = time()
    #print(combinaisons_backtrack(chiffres, k))
    # print(combinaisons_all(chiffres, k))
    end = time()
    print(permutation_any(['a',1, 2]))
    print("dt = {} & dt1 = {}".format(mid - start, end - mid))
