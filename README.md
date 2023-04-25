# H4ALL.ics
This script will create a .ics file with all the games of a team from handball4all.de
***
#  Usage

> ⚠ Make sure Python 3.x is installed on your machine.

1. Install the required libraries: `requests`, `dirtyjson`, `arrow`, and `ics`. You can install them using pip with the command:
     ```shell 
     pip install requests dirtyjson arrow ics
     ```

2. Obtain the Team ID from the Handball4all website. Visit www.handball4all.de and navigate to the site that shows the team's games. From the URL, you can see the corresponding ID:
     `tId` - Team ID (e.g. 720111)

3. Download the script or copy the script into a file and save it as `getGames.py`.

4. Open the command prompt or terminal and navigate to the directory where the script is saved.

5. Run the script using the command `python3 getGames.py` or by running the script.

6. Enter the Team ID when prompted and press Enter.

7. Wait for the script to finish running. The script will create a .ics file with all the team's games and save it in the same directory as the script.

8. Open the .ics file with any calendar software that supports the iCalendar format (such as Google Calendar or Microsoft Outlook) to see the team's games.
    
