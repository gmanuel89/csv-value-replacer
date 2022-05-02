# csv-value-replacer
The application allows to replace values within a CSV file.

The first file that is been asked the user to provide is a CSV file containing the map of values to be replaced, with one column identified as "new" and the other column identified as "old".
The application can detect the word "new" and "old" within the header (in a case-insensitive manner), therefore the columns can be named freely as long as the header contains the two key words (e.g. "new values" - "old values", or "new items" - "old items", or "NEW" - "OLD", etc...).

<img width="269" alt="map csv dialog" src="https://user-images.githubusercontent.com/14137927/166256412-24b2149a-6b02-43df-97a5-8659311c82fd.png">

<img width="83" alt="map csv" src="https://user-images.githubusercontent.com/14137927/166256688-cf90741b-2e8a-4346-94b2-5a0941606332.png">

The second file that is been asked the user to provide is the CSV file to be modified, with the specific values being replaced according to the map provided.

<img width="236" alt="input csv" src="https://user-images.githubusercontent.com/14137927/166257044-a0918b99-d3e6-432a-9588-eaeaef8a74b2.png">

In the worst case scenario, no changes are applied to the files.
