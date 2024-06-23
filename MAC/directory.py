from graphviz import Digraph

# Initialize the Digraph object
dot = Digraph(comment='NAS Directory Structure')

# Define the directory structure
directory_structure = {
    'NAS': {
        'Areas': {
            'Health_Fitness': [
                'Weight_Training', 'Running', 'Yoga', 'Boxing', 'Tennis', 'Cooking', 'Mental_Health'
            ],
            'Professional_Development': [
                'Project_Management', 'Tech_Coordination'
            ],
            'Personal_Development': [
                'Reading', 'Meditation', 'Learning',
                {
                    'Language_Learning': ['English', 'Thai', 'Chinese']
                },
                'Wisdom_Quotes', 'Book_Summaries'
            ],
            'Hobbies': [
                'Pet_Care'
            ],
            'Technology_Digital': [
                'Crypto_Blockchain', 'Website', 'PKM_Strategies', 'Python', 'Cryptocurrency', 'Smart_Home'
            ],
            'Finance': [
                'Investments', 'Net_Worth_Tracking', 'Land_Documents', 'Bank_Accounts', 'Stock_Market', 'Gold', 'Credit_Cards'
            ],
            'Sports': [
                'Soccer',
                {
                    'Tennis': ['Playing', 'Watching']
                }
            ],
            'Personal_Interests': [
                'Music', 'Fragrances', 'Astrology', 'Movies', 'Gaming', 'Chess', 'Style'
            ],
            'Leisure': [
                'Social', 'Traveling'
            ],
            'Business': [
                'Samchai', 'KJSupply', 'ParetoNode'
            ]
        },
        'Resources': {
            'Templates': ['Documents', 'Spreadsheets', 'Presentations'],
            'Research_Papers': ['Health_Fitness', 'Business', 'Technology', 'Personal_Development'],
            'Graphics': ['Logos', 'Icons', 'Photos'],
            'Books_Articles': ['Fiction', 'Non-fiction', 'Journals'],
            'Courses_Tutorials': ['Online_Courses', 'Video_Tutorials', 'Documentation'],
            'Software_Tools': ['Utilities', 'Development_Tools', 'Applications'],
            'Music_Audio': ['Tracks', 'Podcasts', 'Sound_Effects'],
            'Personal_Pictures': ['2024', '2023', '2022', '2021', '2020', 'etc.'],
            'Movies': ['Action', 'Drama', 'Comedy', 'Science_Fiction', 'Documentaries', 'etc.'],
            'City_Information': ['Maps', 'Guides', 'Historical_Data', 'Travel_Tips', 'etc.'],
            'Voice_Recordings': ['Personal', 'Professional'],
            'University_Documents': ['Undergraduate', 'Postgraduate'],
            'Certificates': ['Professional', 'Educational', 'Personal_Achievements'],
            'Audiobooks': ['Fiction', 'Non-fiction'],
            'eBooks': ['Fiction', 'Non-fiction'],
            'Car_Information': [
                {
                    'Car_1': ['Documents', 'Pictures']
                },
                {
                    'Car_2': ['Documents', 'Pictures']
                }
            ],
            'Planning': ['Daily_Planning', 'Weekly_Planning', 'Monthly_Planning', 'Yearly_Planning', 'Project_Planning'],
            'Wishlist': ['Gadgets', 'Books', 'Courses', 'Travel', 'Fitness_Equipment', 'Clothing', 'Home_Appliances'],
            'Theory': ['Scientific_Theory', 'Business_Theory', 'Economic_Theory', 'Philosophical_Theory', 'Psychological_Theory'],
            'Strategy': ['Business_Strategy', 'Investment_Strategy', 'Marketing_Strategy', 'Personal_Development_Strategy', 'Fitness_Strategy', 'Productivity_Strategy']
        }
    }
}

# Function to add nodes and edges
def add_nodes_edges(dot, parent_name, structure):
    for key, value in structure.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for sub_key, sub_value in item.items():
                        dot.node(sub_key)
                        dot.edge(parent_name, sub_key)
                        add_nodes_edges(dot, sub_key, {sub_key: sub_value})
                else:
                    dot.node(item)
                    dot.edge(parent_name, item)
        elif isinstance(value, dict):
            dot.node(key)
            dot.edge(parent_name, key)
            add_nodes_edges(dot, key, value)
        else:
            dot.node(value)
            dot.edge(parent_name, value)

# Add the root node
dot.node('NAS')
# Add nodes and edges
add_nodes_edges(dot, 'NAS', directory_structure['NAS'])

# Render the graph
dot.render('nas_directory_structure', format='png', view=True)
