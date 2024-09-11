import matplotlib.pyplot as plt

# Sample data
labels = ['Missed for Valid Reasons', 'Missed for No Reason']
sizes = [sum(missed_lectures_reason), sum(missed_lectures_no_reason)]
colors = ['skyblue', 'salmon']

# Create a donut chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, startangle=90, wedgeprops=dict(edgecolor='w'), autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.50, fc='white')  # Draw a circle in the center
fig = plt.gcf()
fig.gca().add_artist(centre_circle)  # Add the circle to the chart

# Add title
plt.title('Donut Chart of Total Missed Lectures', fontsize=16)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that the donut is circular
plt.show()
