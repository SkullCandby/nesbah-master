var datatable = $("#leads-table").DataTable();
leads = JSON.parse(leads.replaceAll("None", "null").replace(/'/g, '"'));

for (let i = 0; i < leads.length; i++) {
    datatable.row.add(["0", leads[i]["business_cap"],  leads[i]["number_of_stuff"], leads[i]["regions"], leads[i]["req_service"], 
        `<a href="#" class="btn btn-outline-primary" data-id="${leads[i]["id"]}" data-bs-toggle="modal" data-bs-target="#viewcorporate">View More</a>`
    ]).draw(false);
}

document.getElementById("number-paid-view").textContent = leads.length;
document.getElementById("number-free-view").textContent = allLeadsAmount-leads.length;

function printData(lead) {
    let formControls = document.querySelectorAll('.modal-body input.form-control');
    let fields = ["contact_person", "mobile", "position", "email", "regions", "req_service", "years", "sector", "number_of_stuff", "saudi_stuff", "avg_salary", "legal_form", "business_cap", "number_of_branches", "website", "notes"];

    for (let i = 0; i < formControls.length; i++) {
        formControls[i].value = lead[fields[i]];
    }
}

$("a.btn.btn-outline-primary[data-bs-toggle='modal'][data-bs-target='#viewcorporate']").click(function(){
    let selectedLead = leads.filter(lead => lead["id"].toString() === this.getAttribute("data-id"))[0];  
    printData(selectedLead);
    document.getElementById("btn-see-full-data").setAttribute("data-application-id", this.getAttribute("data-id"));
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