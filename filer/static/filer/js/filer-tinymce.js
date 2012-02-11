(function($) {

    dismissRelatedImageTinyMCELookupPopup = function(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt, filer_serve) {
        var win = tinyMCEPopup.getWindowArg("window");
        URL = filer_serve+chosenId+"/";
        // insert information now
        win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = URL;

        // change width/height & show preview
        if (win.ImageDialog){
            if (win.ImageDialog.getImageData)
                win.ImageDialog.getImageData();
            if (win.ImageDialog.showPreviewImage)
                win.ImageDialog.showPreviewImage(URL);
        }

        // close popup window
        tinyMCEPopup.close();
    };
})(jQuery);