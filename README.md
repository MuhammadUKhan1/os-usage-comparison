# os-usage-comparison

This project analyzes mobile device usage based on the operating system, age, and gender of users. It uses a dataset containing user behavior information and generates pie chart visualizations to display app usage patterns across different demographics.

 **Features**
Filters users based on mobile operating system (Android or iOS).
Segments users by age (above and below 20).
Groups data by gender and calculates total app usage time for each gender.
Visualizes data with pie charts to compare app usage across different demographic groups.

**Dataset**
The dataset, user_behavior_dataset.csv, is located in the csv_file/ folder. It contains the following fields:

Operating System: The user's mobile operating system (Android or iOS).
App Usage Time (min/day): The average time spent on apps per day (in minutes).
Age: The user's age.
Gender: The user's gender.

**Installation Prerequisites**
Make sure you have the following installed:

Python 3.x
Required Python libraries (install via pip):

pip install pandas matplotlib 

 **Cloning the Repository**
Clone the repository to your local machine:
git clone https://github.com/MuhammadUKhan1/os-usage-comparison.git
cd os-usage-comparison/Os-Usage-Analysis/pythonProject

**Running the Analysis**
To run the analysis and generate visualizations:
python MobileUsageAnalysis.py


**Example Visualizations**
Upon running the script, you will see the following pie charts:

Android Users above 20 (by gender)
Android Users below 20 (by gender)
iOS Users above 20 (by gender)
iOS Users below 20 (by gender)

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contributing**
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your changes.
Submit a pull request for review.
For major changes, please open an issue first to discuss your ideas.

**Contact**
If you have any questions or suggestions, feel free to reach out:

Email: izumi.miyamura217@gmail.com
