# csv-value-replacer
The application allows to replace values within a CSV file.

The first file that is been asked the user to provide is a CSV file containing the map of values to be replaced, with one column identified as "new" and the other column identified as "old".
The application can detect the word "new" and "old" within the header (in a case-insensitive manner), therefore the columns can be named freely as long as the header contains the two key words (e.g. "new values" - "old values", or "new items" - "old items", or "NEW" - "OLD", etc...).

![](/images/dialog.png "Map csv dialog")

![](/images/map_csv.png "Map csv")

The second file that is been asked the user to provide is the CSV file to be modified, with the specific values being replaced according to the map provided.

![](/images/dialog2.png "Input csv")

In the worst case scenario, no changes are applied to the files.
