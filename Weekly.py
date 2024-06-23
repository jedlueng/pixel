import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the weekly schedule
week_schedule = {
    'Time': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
             'Boxing Class / Tennis Class / Dog Swimming', 'Flexible / Work/Rest', 'Dog Walk', 
             'Yoga Session / Strength Training', 'Dinner', 'Gaming/Movies', 'Meditate & Stretch', 
             'Talking with Girlfriend', 'Sleep'],
    'Monday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
               'Boxing Class', 'Flexible', 'Dog Walk', 'Yoga Session', 'Dinner', 'Gaming/Movies', 
               'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Tuesday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
                'Tennis Class', 'Work/Rest, socialize dog', 'Dog Walk', 'Yoga Session', 'Dinner', 'Gaming/Movies', 
                'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Wednesday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
                  'Flexible', 'Mental Therapy', 'Dog Walk', 'Strength Training', 'Dinner', 'Gaming/Movies', 
                  'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Thursday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
                 'Tennis Class', 'Work/Rest, socialize dog', 'Dog Walk', 'Yoga Session', 'Dinner', 'Gaming/Movies', 
                 'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Friday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Work', 'Meal Prep', 
               'Dog Swimming', 'Flexible', 'Dog Walk', 'Strength Training', 'Dinner', 'Gaming/Movies', 
               'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Saturday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Flexible', 'Meal Prep', 
                 'Mall Walk & Cafe', 'Meet Family', 'Dog Walk', 'Strength Training', 'Dinner', 'Gaming/Movies', 
                 'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep'],
    'Sunday': ['Wake up', 'Breakfast', 'Nootropics', 'Cold Water', 'Play with Beagle', 'Flexible', 'Meal Prep', 
               'Mall Walk & Cafe', 'Meet Family', 'Dog Walk', 'Rest/Light Activities', 'Dinner', 'Gaming/Movies', 
               'Meditate & Stretch', 'Talking with Girlfriend', 'Sleep']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(week_schedule)

# Convert the DataFrame to a format suitable for plotting
melted_df = df.melt(id_vars='Time', var_name='Day', value_name='Activity')

# Define colors for each activity
unique_activities = melted_df['Activity'].unique()
colors = sns.color_palette('husl', len(unique_activities))
activity_color_map = dict(zip(unique_activities, colors))

# Map colors to activities
melted_df['Color'] = melted_df['Activity'].map(activity_color_map)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each day as a horizontal stacked bar
for day in melted_df['Day'].unique():
    day_data = melted_df[melted_df['Day'] == day]
    ax.barh(day, [1]*len(day_data), left=list(range(len(day_data))), color=day_data['Color'], edgecolor='white', height=0.6)

# Add legend
handles = [plt.Line2D([0], [0], color=activity_color_map[activity], lw=4) for activity in unique_activities]
labels = unique_activities
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.1, 1), ncol=1)

# Customize the plot
ax.set_yticks(range(len(melted_df['Day'].unique())))
ax.set_yticklabels(melted_df['Day'].unique(), fontsize=12)
ax.set_xticks([])
ax.set_xlabel('Activities throughout the day', fontsize=14)
ax.set_title('Weekly Habit Snapshot - June 2024\nJedsada\'s Schedule', fontsize=16, fontweight='bold')

# Add subtitles and personal information
fig.text(0.1, 0.02, 'Name: Jedsada | Month: June 2024', ha='left', fontsize=12)

plt.tight_layout()
plt.show()
