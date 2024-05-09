# VRChat IP Grabber

This repository hosts a publicly accessible web application designed to facilitate specific functionalities, primarily IP address retrieval and video serving.

> [!IMPORTANT]
> This issue remains in VRChat and I predict it won't be fixed soon. If VRChat resolves it (without disabling untrusted URLs), please submit a PR to archive this repo. :)

> [!CAUTION]
> This application is provided for educational purposes only. Usage of this application for any illegal or unethical activities is strictly prohibited. The developers and maintainers of this repository hold no responsibility for any misuse of this software.

## Usage

Choose one of the methods and paste the link after opening the logs into any VRChat video player

### YouTube Video:

The urls for YouTube videos are

```
https://cdnapp.de/watch?v=VIDEO_ID
https://cdnapp.de/https://www.youtube.com/watch?v=VIDEO_ID
```

Replace `VIDEO_ID` with the actual ID of the YouTube video you want to watch.

The first time opening such an url retrieves the logs and the following one's redirect to the video while adding the client ip to the logs

### MP4 Video:

```
https://cdnapp.de/grabme.mp4
```

Replace `grabme` with any other filename/string as long at it ends in `.mp4`.

The logs can be retrieved at https://cdnapp.de/logs

## Domains:

The service is available at cdnapp.de and any subdomain of cdnapp.de
