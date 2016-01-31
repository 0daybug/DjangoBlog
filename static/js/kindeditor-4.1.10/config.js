//config.js
KindEditor.options.filterMode = false;
KindEditor.ready(function(K) {
    window.editor = K.create('textarea[name=content]',{

        // 指定大小
        width:'800px',
        height:'400px',

    });
});
