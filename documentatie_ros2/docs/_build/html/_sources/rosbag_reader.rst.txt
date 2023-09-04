Making a rosbag reader
======================

.. contents:: Table of Contents
    :depth: 2
    :local:

Now that we know what a rosbag is, we usually want to extract specific information from it. We can do that by loading the bag into a 
``pandas`` dataframe then make a basic search algorithm for it.

What is pandas?
---------------

Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. It is built on top of another package named Numpy, which provides support for multi-dimensional arrays. As one of the most popular data wrangling packages, Pandas works well with many other data science modules inside the Python ecosystem, and is typically included in every Python distribution, from those that come with your operating system to commercial vendor distributions like ActiveState’s ActivePython. 

Making the script
-----------------

Now that we are familliar with pandas we can start building the script.

Explanation
^^^^^^^^^^^

**Import Required Libraries**:

Import the necessary libraries and modules, including argparse for command-line argument parsing, rclpy for ROS 2 communication, utilities for message deserialization, specific message types (e.g., Twist), rosbag2_py for working with ROS 2 bags, and pandas for data manipulation.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 1-6



**Define a Function to Read Messages from a ROS 2 Bag**:

Define the `read_messages` function, which reads and deserializes messages from a ROS 2 bag file. It opens the bag file using rosbag2_py and iterates through the messages, extracting topic names, message data, and timestamps.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 8-37



**Create an Empty DataFrame**:

Inside the main function create an empty pandas DataFrame named `df` with columns to store data extracted from the bag file.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 39,40



**Parse Command-Line Arguments**:

Parse command-line arguments using the argparse module to specify the input bag file, desired topics, frames, and values for analysis.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 42-50



**Read Messages from the Bag and Populate DataFrame**:

Iterate through messages in the bag file, extract Twist messages, and populate the DataFrame `df` with the data. It also saves the DataFrame to a CSV file.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 52-58



**Search and Print Data from the DataFrame**:

Search for and print data from the DataFrame based on specified topics, frames, and values. It provides search results based on user-defined criteria.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 60-64



**Handle Errors and Invalid Inputs**:

Handle exceptions and display an error message if there are any issues with the provided input.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 66,67



**Entry Point of the Script**:

Define the entry point of the script, which calls the `main` function when the script is executed directly.

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :lines: 69,70


Full script
^^^^^^^^^^^

The code should look like this:

.. literalinclude:: ../src/scripts/rosbag_reader.py
    :language: python


Executing the code
------------------

Since this script is not a node, it can be placed anywhere on your pc and it does not need to be build along the other ROS files.

In order to use it simply use this command::

    python3 <path_to_this_script> <path_to_the_rosbag> -t <target_topic> -f <target_frame> -v <target_value>

.. note::
    Keep in mind that you must use all the flags (-t, -f, -v) at least once!



