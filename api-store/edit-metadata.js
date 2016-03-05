/* sub will be defined on html/customer/edit.html on the subscription edit
   page.
 */

function update_metadata() {
    var metadata = {
            "Date of birth" : "2000-01-01",
    }

    $.ajax({
        url: '/v1/store/api/subscriptions/{{sub.id}}/metadata/',
        contentType: 'application/json',
        type: 'POST',
        data: JSON.stringify(metadata),
        success: function(data) {
            console.log(data)
            window.location = "/customer/account";
        }
    })
}

