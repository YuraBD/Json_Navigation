# Json_navigation
This is program to navigate through json object of friends of given twitter user.
To start a program run json_navigation.py

## Usage
```zsh
>>> python json_navigation.py
Enter username: @BarackObama
Enter number of friends to get: 4
Enter bearer token: AAA...6d0
This is dictionary. Enter a key index from list below or -2 to end a program: 
0) users   1) next_cursor   2) next_cursor_str   3) previous_cursor   4) previous_cursor_str   5) total_count
Key index: 0
This is list. Do you want to display the entire list?
0) Yes   1) No
Choose an option: 1
Enter an index in range from 0 to 3 or -1 to return back, -2 to end a program
Enter an index: 1
This is dictionary. Enter a key index from list below or -1 to return back, -2 to end a program: 
0) id   1) id_str   2) name   3) screen_name   4) location   5) description   6) url   7) entities   8) protected   9) followers_count   10) friends_count   11) listed_count   12) created_at   13) favourites_count   14) utc_offset   15) time_zone   16) geo_enabled   17) verified   18) statuses_count   19) lang   20) status   21) contributors_enabled   22) is_translator   23) is_translation_enabled   24) profile_background_color   25) profile_background_image_url   26) profile_background_image_url_https   27) profile_background_tile   28) profile_image_url   29) profile_image_url_https   30) profile_banner_url   31) profile_link_color   32) profile_sidebar_border_color   33) profile_sidebar_fill_color   34) profile_text_color   35) profile_use_background_image   36) has_extended_profile   37) default_profile   38) default_profile_image   39) following   40) follow_request_sent   41) notifications   42) muting   43) blocking   44) blocked_by   45) translator_type
Key index: 4
This is str. Do you want to display it?
0) Yes   1) No
Choose an option: 0

 New York, NY 

This is the end of the file.
Enter -1 to return back or -2 to end a program
```

## License
[MIT](https://choosealicense.com/licenses/mit/)