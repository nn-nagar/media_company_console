from django.urls import path
from myapp.views import ShowDetailListView, ShowDetailView, ShowDetailCreateView, \
    ShowDetailUpdateView, EpisodeDetailUpdateView, EpisodeDetailDeleteView, EpisodeDetailCreateView, EpisodeDetailView, \
    EpisodeDetailListView, ShowDetailDeleteView, FileUpload

urlpatterns = [

    path(
        "show/shows_detail_list/",
        ShowDetailListView.as_view(),
        name="shows-detail-list",
    ),
    path(
        "show/show_detail/<uuid:show_uuid>/",
        ShowDetailView.as_view(),
        name="show-detail",
    ),
    path(
        "show/shows_detail_create/",
        ShowDetailCreateView.as_view(),
        name="show-detail-create",
    ),
    path(
        "show/shows_detail_delete/<uuid:show_uuid>/",
        ShowDetailDeleteView.as_view(),
        name="show-detail-delete",
    ),
    path(
        "show/shows_detail_update/<uuid:show_uuid>/",
        ShowDetailUpdateView.as_view(),
        name="show-detail-update",
    ),     ######### There is episode endpoints

    path(
        "episode/episodes_detail_list/",
        EpisodeDetailListView.as_view(),
        name="episodes-detail-list",
    ),
    path(
        "episode/episodes_detail/<uuid:episode_uuid>/",
        EpisodeDetailView.as_view(),
        name="episodes-detail",
    ),
    path(
        "episode/episodes_detail_create/",
        EpisodeDetailCreateView.as_view(),
        name="episodes-detail-create",
    ),
    path(
        "episode/episodes_detail_delete/<uuid:episode_uuid>/",
        EpisodeDetailDeleteView.as_view(),
        name="episodes-detail-delete",
    ),
    path(
        "episode/episodes_detail_update/<uuid:episode_uuid>/",
        EpisodeDetailUpdateView.as_view(),
        name="episodes-detail-update",
    ),

    path(
        "fileupload/<str:doc_type>/",
        FileUpload.as_view(),
        name="fileupload",
    ),

]
