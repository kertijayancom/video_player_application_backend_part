# video_player_application_backend_part
this is a fully video player application - backend part - using django framework


# **instalation**



for better experience, please using virtual environment and install requirement.txt on relief_backend folder

Install the gem:

```bash
conda create --name <env> --file requirements.txt
```

## **How it works**


A simple Django API to store the user's history and bookmarks through two entities: History and Bookmark.


## **LIST API**

The API provide 4 routes to:
- List all videos in the history
- Add a video to the history
- List all videos in the bookmarks
- Add a video to the bookmarks

**URL and Port**
it works on port 8000 and using local development url such as localhost or 127.0.0.1


# **Example of API Request and Response**

1. List all videos in the history

request URL, without header, only param [`page`] starting from 1 . maximum 100 item per page. you can change the limit per page on class [`LargeResultsSetPagination`] inside the relief_backend/relief_backend/views.py file.

```bash
GET - http://localhost:8000/histories/?page=1
```

response URL
```bash
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "http://localhost:8000/histories/e8edde40-93eb-4d0d-8a29-f06b3d26f14f/",
      "video_id": "EEGHJRU_BXA",
      "video_url": "https://www.youtube.com/watch?v=EEGHJRU_BXA",
      "created_at": "2020-12-24T05:33:28.341697Z"
    },
    {
      "url": "http://localhost:8000/histories/48537c3b-e10b-4481-8e5a-76995e69b612/",
      "video_id": "EEGHJRU_BXA",
      "video_url": "https://www.youtube.com/watch?v=EEGHJRU_BXA",
      "created_at": "2020-12-24T05:33:29.101188Z"
    }
  ]
}
```

2. Add a video to the history

request URL

```bash
POST - http://localhost:8000/histories/
```

```bash
Parameter Multipart-form

video_url
video_id
```

for example video_url https://www.youtube.com/watch?v=EEGHJRU_BXA and video_id EEGHJRU_BXA

response URL - 201 Success Created
```bash
{
  "url": "http://localhost:8000/histories/71c2681d-df38-4fb2-bd4d-5ebb70298166/",
  "video_id": "EEGHJRU_BXA",
  "video_url": "https://www.youtube.com/watch?v=EEGHJRU_BXA",
  "created_at": "2020-12-24T06:41:29.080377Z"
}
```

3. List all videos in the bookmarks

request URL, without header, only param [`page`] starting from 1 . limit item per page using a global setting from Django Rest Framework on [`settings.py`] file. 

```bash
GET - http://localhost:8000/bookmarks/?page=1
```

response URL
```bash
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "http://localhost:8000/bookmarks/5dadfbca-e4d3-4d18-93cf-b375d34a271d/",
      "video_id": "EEGHJRU_BXA",
      "video_url": "https://www.youtube.com/watch?v=EEGHJRU_BXA",
      "created_at": "2020-12-24T05:33:02.622728Z"
    },
    {
      "url": "http://localhost:8000/bookmarks/3dd56049-df96-462c-a5a9-d5c598c87e23/",
      "video_id": "vbqLytlKB0g",
      "video_url": "https://www.youtube.com/watch?v=vbqLytlKB0g",
      "created_at": "2020-12-24T05:49:31.587907Z"
    }
  ]
}
```

you can change the limit per page on this variable. default is 10
```bash
REST_FRAMEWORK = {
    ....    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    ....
}
```
4. Add a video to the bookmarks

request URL

```bash
POST - http://localhost:8000/bookmarks/
```

```bash
Parameter Multipart-form

video_url
video_id
```

for example video_url https://www.youtube.com/watch?v=x4T96RReg4c and video_id x4T96RReg4c.
if request contain duplicate data on the database, it is still acceptable, only renew the datetime field [`created_at`].

response URL - 201 Success Created
```bash
{
  "url": "http://localhost:8000/bookmarks/37e7305d-8c47-4cf5-a7e7-55afca1b1782/",
  "video_id": "x4T96RReg4c",
  "video_url": "https://www.youtube.com/watch?v=x4T96RReg4c",
  "created_at": "2020-12-24T08:55:57.757316Z"
}
```
all primary key field is using [UUID format reference](https://docs.djangoproject.com/en/3.1/ref/models/fields/#uuidfield) for better security experience.
