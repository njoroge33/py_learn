# The determinant of a 2x2 matrix is the product of the elements on the main diagonal minus
#  the product of the elements of the main diagonal
# Write a function determinant(m, n), that takes in two tuples of exactly two elements each and
#  returns the determinant of the 2x2 matrix formed by the tuples?
# for more info on this quiz, go to this url: http://www.programmr.com/determinant-2x2-matrix


def determinant(tup_m, tup_n):
    for i in tup_m:
        det = (tup_m[0] * tup_n[1]) - (tup_m[1] * tup_n[0])
        return det


if __name__ == "__main__":
    print(determinant((4, 6), (7, 8)))
