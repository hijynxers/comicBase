# database_location = '/var/www/myWebsite/myWebsite/comics_database.db'
database_location = 'comics_database.db'


def convert_title(issue_name, volume):
    issue_name = issue_name.lower()
    table_title = issue_name.lstrip().rstrip().replace(' ', '_')+'_'+str(volume)
    return table_title

def revert_title(title_name):
    title_info = title_name.split('_')
    volume = title_info[-1]  # the last one is the volume information
    issue_list = title_info[0:-1] # issue name is everything else
    issue = ''
    # reconstruct the issue name
    for word in issue_list:
        if issue != '':
            issue += ' '
        issue += word
    issue = issue.title()   # then make first lettes capital
    return issue, volume
