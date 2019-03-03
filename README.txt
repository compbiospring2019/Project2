------------------
Usage Instructions
------------------

Linux and Windows instructions:
To run this program, unzip our project. Change directories
to our project directory (the directory containing decision_tree.py).

Then, to train the decision tree, enter

python train_and_evaluate.py <fasta_directory> <sa_directory>

in the command line, where fasta_directory is the directory with
the fasta files and sa_directory is the directory with
the sa files for training and evaluating.
This will create a file called model.json in the current directory.

To classify a new sequence, make sure you've trained the decision
tree (above). Then, enter

python classify_sequence.py <fasta_file_name> [<sa_file_name> (optional)]

in the command line, where fasta_file_name is the absolute file path
(in double quotes, if you have spaces in your path names) of the
FASTA sequence to be classified. The sa_file_name is optional.
If provided, it will pretty-print the predicted outcomes and the
real values. Otherwise, it will just print the predicted outcomes.

Notes:
If your python executable has a different name, use that name
instead of 'python'.
Paths were tested with absolute paths, enclosed in double quotes.
Tested with python2.7 and python3.6.
