$(function(){
    var url = '/users'
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url,
            insertUrl: url,
            updateUrl: url,
            deleteUrl: url,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),

        editing: {
            allowUpdating: true,
            allowDeleting: true,
            allowAdding: true
        },
        
        paging: {
            pageSize: 12
        },

        pager: {
            showPageSizeSelector: false,
            allowedPageSizes: [8, 12, 20]
        },
        
        columns: [{
            dataField: "id",
            dataType: "number",
            allowEditing: false
        }, {
            dataField: "email"
        }, {
            dataField: "name"
        }, {
            dataField: "fullname"
        }, {
            dataField: "username"
        },{
            dataField: "password"
        },],

    }).dxDataGrid("instance");
});
