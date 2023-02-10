var datatable = $("#leads-table").DataTable();
leads = JSON.parse(leads.replaceAll("None", "null").replace(/'/g, '"'));

let regions = [
    "Eastern",
    "Western",
    "Southern",
    "Northern"
];

let requiredService = [
    "Company Enrollment & Staff Offering",
    "Company Financing Services",
    "Account Opening",
    "Offering Discount to Banking Customers"
];

let sector = [
    "Private",
    "Government",
    "Semi Government"
];

let legalForm = [
    "Joint Stock Company/Public Traded",
    "Sole Proprietorship",
    "Limited and General Partnership"
]

for (let i = 0; i < leads.length; i++) {
    let date = new Date(leads[i]["date_created"]);
    date = new Intl.DateTimeFormat('en-NL', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);
    
    document.getElementById("date").textContent = `Date (${Intl.DateTimeFormat().resolvedOptions().timeZone})`;

    let not_seen = leads.length - leads[i]["count_viewed"];

    let buttonPaid = `<a href="#"><span class="badge bg-success">${leads[i]["count_paid"]}</span></a>`;
    let buttonJustViewed = `<a href="#"><span class="badge bg-warning">${leads[i]["count_viewed"]}</span></a>`;
    let buttonNotSeen = `<a href="#"><span class="badge" style="background-color: #b02a37;">${not_seen}</span></a>`;
    let buttonViewMore = `<a href="#" class="btn btn-outline-primary" data-id="${leads[i]["id"]}" data-bs-toggle="modal" data-bs-target="#viewcorporate">View More</a>`;

    leads[i]["regions"] = regions[leads[i]["regions"]];
    leads[i]["req_service"] = requiredService[leads[i]["req_service"]];
    leads[i]["sector"] = sector[leads[i]["sector"]];
    leads[i]["legal_form"] = legalForm[leads[i]["legal_form"]];
    console.log(leads[i]["company_name"]);
    datatable.row.add([leads[i]["company_name"], date,  leads[i]["sector"], "Not available yet", buttonPaid, buttonJustViewed, buttonNotSeen, buttonViewMore]).draw(false);
}

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
    console.log(selectedLead["id"]);
    document.getElementById("btn-see-full-data").setAttribute("data-application-id", this.getAttribute("data-id"));
});