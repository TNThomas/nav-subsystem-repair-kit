from scoring import score_corrupt_lines, score_incomplete_lines

input_file: str = "input.txt"
test_file: str = "test.txt"

def main():
    with open(input_file) as infile:
#        corrupt_score = score_corrupt_lines(infile)
#        print(f"Corrupt Lines Total Score: {corrupt_score}")
        incomplete_score = score_incomplete_lines(infile)
        print(f"Incomplete Lines Median Score: {incomplete_score}")


if __name__ == "__main__":
	main()
