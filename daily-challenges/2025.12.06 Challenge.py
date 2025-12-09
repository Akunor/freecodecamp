# start of main.py

import datetime

def format_date(date_string):
    date = datetime.datetime.strptime(date_string, '%B %-d, %Y')
    formatted = date.strftime("%Y-%m-%d")
    # Submission not working despite code being functional so not submitted on FCC's website as usual:
    
    return formatted

# end of main.py

'''
// start of main.js

function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const formatted = `${year}-${month}-${day}`;
    // Submission not working despite code being functional so not submitted on FCC's website as usual:
    
    return formatted;
}

// end of main.js
'''