import csv
import sys
import csv


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Correct Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable which will be a dict.
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        reader_file = csv.DictReader(file)

        # create a header of the fieldnames of the STR names
        str_list = reader_file.fieldnames[1:]

        # TODO: Read DNA sequence into a variable
        sequence_name = sys.argv[2]
        with open(sequence_name, 'r') as sequence:
            lines = sequence.read()

        # iterate through each row of the dictionary
        for row in reader_file:

            # assign for each row the first column (name) to the variable name
            name = row['name']

            # iterate through each STR value inside the str_list header
            for current_str in str_list:
                is_found = True

                # calculate the highest count of that STR in the DNA sequence file
                longest = longest_match(lines, current_str)

                # for the current row, check if the current person has the same count of current STR
                if int(row[current_str]) != longest:
                    is_found = False
                    break

            # if the current row has all the highest STR count, we found who the DNA belongs too
            if is_found:
                print(name)
                sys.exit(0)

    # if no person has all the highest count then no match
    print('No match')


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
