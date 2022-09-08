(function () {
    let dropArea = document.querySelector('.file-drop-area');
    let input = dropArea.querySelector('.file-drop-input'),
        message = dropArea.querySelector('.file-drop-message'),
        icon = dropArea.querySelector('.file-drop-icon'),
        selectButton = dropArea.querySelector('.file-drop-btn'),
        subimitButton = dropArea.querySelector('.submit-button'),
        invalidFileSize = document.querySelector('.invalidFileSize'),
        invalidFileType = document.querySelector('.invalidFileType'),
        maxNomberFile = document.querySelector('.maxFile');


    message.innerHTML = "glissez deposez ici pour televerser";

    selectButton.addEventListener('click', function () {
        input.click();
    });



    input.addEventListener('change', function () {
        // # preview image at the input file
        let file = input.files[0];
        if ( file && ((file.type == "image/jpeg") || (file.type == "image/png"))) {
            let reader = new FileReader();

            reader.onload = function (e) {
                let fileData = e.target.result;
                let fileName = file.name;
                message.innerHTML = fileName;

                if (fileData.startsWith('data:image')) {
                    let image = new Image();
                    image.src = fileData;

                    image.onload = function () {
                        // CSS is already added in the style script
                        icon.className = 'file-drop-preview img-thumbnail rounded';
                        icon.appendChild(image)
                    };
                }
            };

            reader.readAsDataURL(file);



        }
        // # input field validation
        if (!file) { // This is VERY unlikely, browser support is near-universal
            console.error("This browser doesn't seem to support the `files` property of file inputs.");

        } else if (file) {

            // display the submit button
            subimitButton.style.display = "block";

            // Check filesize is over 1 mb(1000000 bytes)
            if (file.size > 5000000) {
                // show a warning message
                invalidFileSize.style.display = "block";

                // Check file type must be only PNG, JPEG and JPG
            } else if (!((file.type == "image/jpeg") || (file.type == "image/png"))) {
                // show a warning message
                invalidFileType.style.display = "block";

            } else {
                invalidFileSize.style.display = "none";
                invalidFileType.style.display = "none";
            }
        }

        if(file > 0 ){
        }


    });
})();
