var datatable = $("#leads-table").DataTable();
leads = JSON.parse(leads.replaceAll("None", "null").replace(/'/g, '"'));

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

    console.log(date);
    let buttonPaid = `<a href="#"><span class="badge bg-success">1</span></a>`;
    let buttonJustViewed = `<a href="#"><span class="badge bg-warning">1</span></a>`;
    let buttonNotSeen = `<a href="#"><span class="badge" style="background-color: #b02a37;">0</span></a>`;
    let buttonViewMore = `<a href="#" class="btn btn-outline-primary" data-id="${leads[i]["id"]}" data-bs-toggle="modal" data-bs-target="#viewcorporate">View More</a>`;
    datatable.row.add([leads[i]["user_id"], date,  leads[i]["sector"], "Not available yet", buttonPaid, buttonJustViewed, buttonNotSeen, buttonViewMore]).draw(false);
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