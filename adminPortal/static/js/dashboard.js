(function($) {
  'use strict';
  $(function() {
    if ($("#leads").length) {
      var areaData = {
        labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        datasets: [
          {
            data: [0, 0, 0, 0, 0, 0, 0],
            borderColor: [
              '#D43F8D'
            ],
            borderWidth: 2,
            fill: false,
            label: "leads"
          }
        ]
      };

      let maxLeadsList = 1;
      let minLeadsList = 0;
      let leadsStepSize = maxLeadsList;

      if ($('#my-data').data().leads.length != undefined) {
        let leadsList = JSON.parse($('#my-data').data().leads.replace(/'/g, '"'));
      
      
        // loop through week days, if there is data available for that day, set it to the value
        for (let i = 0; i < areaData.labels.length; i++) {
          let weekDay = areaData.labels[i];

          if (leadsList[weekDay] != undefined) {
            areaData.datasets[0].data[i] = leadsList[weekDay];

            if (leadsList[weekDay] > maxLeadsList) {
              maxLeadsList = leadsList[weekDay];
            } 
          }
        }

        // get the highest divisor of the maximum users value
        for (let i = maxLeadsList-1; i > 0; i--) {
          if (maxLeadsList % i == 0) {
            leadsStepSize = i;
          }
        }
      }

      var areaOptions = {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          filler: {
            propagate: false
          }
        },
        scales: {
          xAxes: [{
            display: true,
            ticks: {
              display: true,
              padding: 10,
              fontColor:"#6C7383"
            },
            gridLines: {
              display: false,
              drawBorder: false,
              color: 'transparent',
              zeroLineColor: '#eeeeee'
            }
          }],
          yAxes: [{
            display: true,
            ticks: {
              display: true,
              autoSkip: false,
              maxRotation: 0,
              stepSize: leadsStepSize,
              min: minLeadsList,
              max: maxLeadsList,
              padding: 18,
              fontColor:"#6C7383"
            },
            gridLines: {
              display: true,
              color:"#f2f2f2",
              drawBorder: false
            }
          }]
        },
        legend: {
          display: false
        },
        tooltips: {
          enabled: true
        },
        elements: {
          line: {
            tension: .35
          },
          point: {
            radius: 0
          }
        }
      }
      var revenueChartCanvas = $("#leads").get(0).getContext("2d");
      var revenueChart = new Chart(revenueChartCanvas, {
        type: 'line',
        data: areaData,
        options: areaOptions
      });
    }

    if ($("#application-status").length) {

      let opened = allunlockedleads.length;
      let pending = leadids.length - opened;

      var doughnutPieData = {
        datasets: [{
          data: [opened, pending],
          backgroundColor: [
            '#0774F8',
            '#D43F8D'
          ],
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
          'opened',
          'pending',
        ]
      };
      var doughnutPieOptions = {
        responsive: true,
        animation: {
          animateScale: true,
          animateRotate: true
        }
      };

      var doughnutChartCanvas = $("#application-status").get(0).getContext("2d");
      var doughnutChart = new Chart(doughnutChartCanvas, {
        type: 'doughnut',
        data: doughnutPieData,
        options: doughnutPieOptions
      });
    }

    // if ($("#no_of_applications").length) {
    //   var data = {
    //     labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    //     datasets: [
    //       {
    //         data: [3, 10, 7, 16, 6.8, 11, 8],
    //         backgroundColor: 'green',
    //         width: 10,
    //         label: "Total Application"
    //       }
    //     ]
    //   };
    //   var options = {
    //     scales: {
    //       yAxes: [{
    //         ticks: {
    //           beginAtZero: true,
    //           max : 18
    //         }
    //       }]
    //     },
    //     legend: {
    //       display: false
    //     },
    //     elements: {
    //       point: {
    //         radius: 0
    //       }
    //     }
    //   };
    //   var barChartCanvas = $("#no_of_applications").get(0).getContext("2d");
    //   // This will get the first returned node in the jQuery collection.
    //   var barChart = new Chart(barChartCanvas, {
    //     type: 'bar',
    //     data: data,
    //     options: options
    //   });
    // }

    if ($("#user-growth").length) {
      var areaData = {
        labels: ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"],
        datasets: [
          {
            data: [0, 0, 0, 0, 0, 0, 0],
            borderColor: [
              '#D43F8D'
            ],
            borderWidth: 2,
            fill: false,
            label: "user growth"
          }
        ]
      };

      let maxUserList = 1;
      let minUserList = 0;
      let usersStepSize = maxUserList;

      if ($('#my-data').data().users.length != undefined) {
        let usersList = JSON.parse($('#my-data').data().users.replace(/'/g, '"'));        
        
        // loop through week days, if there is data available for that day, set it to the value
        for (let i = 0; i < areaData.labels.length; i++) {
          let weekDay = areaData.labels[i];
  
          if (usersList[weekDay] != undefined) {
            areaData.datasets[0].data[i] = usersList[weekDay];
  
            if (usersList[weekDay] > maxUserList) {
              maxUserList = usersList[weekDay];
            } 
          }
        }
  
        // get the highest divisor of the maximum users value
        for (let i = maxUserList-1; i > 0; i--) {
          if (maxUserList % i == 0) {
            usersStepSize = i;
          }
        }
      }
      

      var areaOptions = {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          filler: {
            propagate: false
          }
        },
        scales: {
          xAxes: [{
            display: true,
            ticks: {
              display: true,
              padding: 10,
              fontColor:"#6C7383"
            },
            gridLines: {
              display: false,
              drawBorder: false,
              color: 'transparent',
              zeroLineColor: '#eeeeee'
            }
          }],
          yAxes: [{
            display: true,
            ticks: {
              display: true,
              autoSkip: false,
              maxRotation: 0,
              stepSize: usersStepSize,
              min: minUserList,
              max: maxUserList,
              padding: 18,
              fontColor:"#6C7383"
            },
            gridLines: {
              display: true,
              color:"#f2f2f2",
              drawBorder: false
            }
          }]
        },
        legend: {
          display: false
        },
        tooltips: {
          enabled: true
        },
        elements: {
          line: {
            tension: .35
          },
          point: {
            radius: 0
          }
        }
      }
      var revenueChartCanvas = $("#user-growth").get(0).getContext("2d");
      var revenueChart = new Chart(revenueChartCanvas, {
        type: 'line',
        data: areaData,
        options: areaOptions
      });
    }

    function format ( d ) {
      // `d` is the original data object for the row
      return '<table cellpadding="5" cellspacing="0" border="0" style="width:100%;">'+
          '<tr class="expanded-row">'+
              '<td colspan="8" class="row-bg"><div><div class="d-flex justify-content-between"><div class="cell-hilighted"><div class="d-flex mb-2"><div class="mr-2 min-width-cell"><p>Policy start date</p><h6>25/04/2020</h6></div><div class="min-width-cell"><p>Policy end date</p><h6>24/04/2021</h6></div></div><div class="d-flex"><div class="mr-2 min-width-cell"><p>Sum insured</p><h5>$26,000</h5></div><div class="min-width-cell"><p>Premium</p><h5>$1200</h5></div></div></div><div class="expanded-table-normal-cell"><div class="mr-2 mb-4"><p>Quote no.</p><h6>Incs234</h6></div><div class="mr-2"><p>Vehicle Reg. No.</p><h6>KL-65-A-7004</h6></div></div><div class="expanded-table-normal-cell"><div class="mr-2 mb-4"><p>Policy number</p><h6>Incsq123456</h6></div><div class="mr-2"><p>Policy number</p><h6>Incsq123456</h6></div></div><div class="expanded-table-normal-cell"><div class="mr-2 mb-3 d-flex"><div class="highlighted-alpha"> A</div><div><p>Agent / Broker</p><h6>Abcd Enterprices</h6></div></div><div class="mr-2 d-flex"> <img src="../../images/faces/face5.jpg" alt="profile"/><div><p>Policy holder Name & ID Number</p><h6>Phillip Harris / 1234567</h6></div></div></div><div class="expanded-table-normal-cell"><div class="mr-2 mb-4"><p>Branch</p><h6>Koramangala, Bangalore</h6></div></div><div class="expanded-table-normal-cell"><div class="mr-2 mb-4"><p>Channel</p><h6>Online</h6></div></div></div></div></td>'
          '</tr>'+
      '</table>';
  }
  
  });
})(jQuery);


let parsedData = {};
let dataArray = bankusers.slice(1, -1).split(', ');

dataArray.forEach(function(item) {
    let split = item.split(': ');
    parsedData[split[0]] = split[1].replace(/['"]+/g, '');
});

for (let key in parsedData) {
  document.getElementsByClassName("icon-data-list")[0].innerHTML += 
  `
  <li>
    <div class="d-flex">
      <p class="text-info mb-1">${parsedData[key]}</p>
    </div>
  </li>
  `
}