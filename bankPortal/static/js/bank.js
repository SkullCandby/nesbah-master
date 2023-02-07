var datatable = $("#leads-table").DataTable();
leads = JSON.parse(leads.replaceAll("None", "null").replace(/'/g, '"'));
//unlocked = JSON.parse(unlocked.replace(/'/g, '"'));

for (let i = 0; i < leads.length; i++) {
    if (!unlocked.includes(leads[i]["id"].toString())) {
        datatable.row.add(["0", leads[i]["business_cap"],  leads[i]["number_of_stuff"], leads[i]["regions"], leads[i]["req_service"], 
        `<a href="#" class="btn btn-outline-primary" data-id="${leads[i]["id"]}" data-bs-toggle="modal" data-bs-target="#viewcorporate">View More</a>`
        ]).draw(false);
    } 
}

function printData(lead) {
    let formControls = document.querySelectorAll('.modal-body input.form-control');
    let fields = ["contact_person", "mobile", "position", "email", "regions", "req_service", "years", "sector", "number_of_stuff", "saudi_stuff", "avg_salary", "legal_form", "business_cap", "number_of_branches", "website", "notes"];

    for (let i = 0; i < formControls.length; i++) {
        formControls[i].value = lead[fields[i]];
    }

    $("#btn-see-full-data").show();
}

$("a.btn.btn-outline-primary[data-bs-toggle='modal'][data-bs-target='#viewcorporate']").click(function(){
    let selectedLead = leads.filter(lead => lead["id"].toString() === this.getAttribute("data-id"))[0];  
    printData(selectedLead);
    id = selectedLead["id"]
    console.log(id);
    document.getElementById("btn-see-full-data").setAttribute("data-application-id", this.getAttribute("data-id"));
    
    $.ajax({
        type: "POST",
        url: "/bank/view_application/",
        contentType: 'application/json; charset=utf-8',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        data: JSON.stringify({view_application: id}),
        success: function() {
            console.log(`${id} viewed`);
        }
    });
});

$("#company-revenue-filter").on("change", function() {
    let regex = "";

    switch ($(this).val()) {
        case "2":
            // 0 - 1000000
            regex = '^[0-9]{1,6}$';
            break;
        case "3":
            // 1000000 - 10000000
            regex = '^1[0-9]{6}$';
            break;
        case "4":
            // 10000000 - 50000000
            regex = '^[1-4][0-9]{7}$';
            break;
        case "5":
            // > 50000000 
            regex = '^5[0-9]{7,}$';
            break;
        default:
            regex = '^[0-9]+$';
            break;
    }

    datatable.column(1).search(regex, true, false).draw();
});

$("#no-staff-filter").on("change", function() {
    let regex = "";

    switch ($(this).val()) {
        case "2":
            // 0 - 1000
            regex = '^([0-9]|[1-9][0-9]{1,2})$';
            break;
        case "3":
            // 1000 - 5000
            regex = '^(1[0-9]{3}|[2-4][0-9]{3}|5000)$';
            break;
        case "4":
            // 5000 - 10000
            regex = '^(5[0-9]{3}|[6-9][0-9]{3}|10000)$';
            break;
        case "5":
            // > 10000 
            regex = '^[1-9][0-9]{4,}$';
            break;
        default:
            regex = '^[0-9]+$';
            break;
    }
    
    datatable.column(2).search(regex, true, false).draw();
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

$("#btn-see-full-data").click(function() {
    id = this.getAttribute("data-application-id");
    $.ajax({
        type: "POST",
        url: "/bank/see-full-data/",
        contentType: 'application/json; charset=utf-8',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        data: JSON.stringify({application_id: id}),
        success: function(response) {
            printData(response[0])
            $("#btn-see-full-data").hide();
            parent = $(`a.btn.btn-outline-primary[data-id='${id}']`).parents("tr");
            console.log(parent);
            datatable.row(parent).remove().draw();
        }
    });
});