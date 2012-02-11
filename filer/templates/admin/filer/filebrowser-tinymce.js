function djangoFileBrowser(field_name, url, type, win) {
    //type = "file_ptr";
    console.log(type);
    var url = "{{ filer_url }}?pop=1&tinymce=1&type=" + type;

    tinyMCE.activeEditor.windowManager.open(
        {
            'file': url,
            'width': 820,
            'height': 500,
            'resizable': "yes",
            'scrollbars': "yes",
            'inline': "no",
            'close_previous': "no"
        },
        {
            'window': win,
            'input': field_name,
            'editor_id': tinyMCE.selectedInstance.editorId
        }
    );
    return false;
}
