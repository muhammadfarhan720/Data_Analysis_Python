"""
@author: << Muhammad Farhan Azmine >>
"""

input_file = r"C:\Users\azmin\Downloads\sequences0.csv"


# input_file = r"C:\Users\azmin\Downloads\sequences1.csv"
# input_file = r"C:\Users\azmin\Downloads\sequences2.csv"
# input_file = r"C:\Users\azmin\Downloads\sequences3.csv"



def read_and_parse_file(filename):
    sequences = []
    with open(filename) as datafile:

        for line in datafile.readlines():

            seq = {}

            # Separate the line into individual tokens at each comma
            parsed_line = line.strip().split(',')

            # Skip the header line
            if parsed_line[0] != "SeqID":

                # Store the sequence ID and amino acid strings
                seq["SeqID"] = parsed_line[0]
                seq["Sequence"] = parsed_line[1]

                # Create a line and store the experimental results
                results = []
                for idx in range(2, len(parsed_line)):
                    results.append(float(parsed_line[idx]))
                seq["Experiments"] = results

                # Add the completed dictionary into the sequences list
                sequences.append(seq)

    # Return all sequences
    return sequences


########################################################
# Write your functions here

def number_of_experiments (data):

    number_exp = len(data)
    return number_exp

def length_of_sequence (data,idx):
    if((idx>=0) and (idx<number_of_experiments(data)) and (type(idx)==int)):
        return number_of_experiments(data[idx]["Sequence"])

def average_sequence_length(data):
    average=0
    for key in range(0,(number_of_experiments(data))):
        average=average+length_of_sequence(data,key)
    # print(average)
    # print(number_of_experiments(data))
    return (average/number_of_experiments(data))

def experiment_result(data, idx, exp):
    if((type(idx)==int) and (type(exp)==int)):
        if((0<=idx < number_of_experiments(data)) and (0<=exp<number_of_experiments(data[idx]["Experiments"])) ):
            return data[idx]["Experiments"][exp]

def individual_experiment_average(data,idx):
    if ((0 <= idx < number_of_experiments(data)) and (type(idx)==int)):
        return (sum(data[idx]["Experiments"])/number_of_experiments(data[idx]["Experiments"]))

def all_experiment_average(data):
    average_sum=0
    for key in range(0,(number_of_experiments(data))):
        average_sum=(individual_experiment_average(data,key))+average_sum
    return (average_sum/number_of_experiments(data))


def longest_experiment_average(data):
    temp_swap=0
    for idx in range(0,number_of_experiments(data)):

        avg_exp=individual_experiment_average(data,idx)
        if(avg_exp>temp_swap):
            temp_swap=avg_exp
            temp_index=idx
    return (data[temp_index]["SeqID"])






########################################################


def main():
    # Load and parse the input file into a list of dictionaries
    all_data = read_and_parse_file(input_file)


    # Here are some data access examples for using the all_data list of
    # dictionaries:

    # Get dictionary #5 of sequences0.csv.
    # Returns {
    #             'SeqID': 'V1sj0De90ph1sI2F13F',
    #             'Sequence': 'TATCGAATGATTGACT',
    #             'Experiments': [14.870597056174102, 7.64767033845676]
    #         }
    print(all_data[5])

    # Get the SeqID associated with dictionary #4 of sequences0.csv.
    # Returns 5Rckc1puuQWLHacWobd
    print(all_data[4]["SeqID"])

    # Get the first experiment value of dictionary #2 of sequences0.csv.
    # Returns 12.360819506572707
    print(all_data[2]["Experiments"][0])

    # Get the number of experiments in dictionary #7 of sequences0.csv (this
    # is) also the number of experiments for every dictionary in the file.
    # Returns 2
    print(len(all_data[7]["Experiments"]))


    ########################################################
    # Test your functions here

    print(number_of_experiments(all_data))

    print(length_of_sequence(all_data, 3))


    print(length_of_sequence(all_data,1))

    print(average_sequence_length(all_data))

    print(experiment_result(all_data, 1, 1))

    print(individual_experiment_average(all_data, 6))

    print(all_experiment_average(all_data))

    print(longest_experiment_average(all_data))

    ########################################################


if __name__ == "__main__":
    main()