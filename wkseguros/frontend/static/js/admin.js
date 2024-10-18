// Graph
var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ],
    datasets: [
      {
        data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
        lineTension: 0,
        backgroundColor: "transparent",
        borderColor: "#007bff",
        borderWidth: 4,
        pointBackgroundColor: "#007bff",
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: false,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
  },
});


document.addEventListener("DOMContentLoaded", function() {
  const links = document.querySelectorAll('#sidebarMenu .list-group-item');
  
  // Recuperar o estado 'active' do localStorage
  const activeLink = localStorage.getItem('activeLink');
  if (activeLink) {
    document.querySelector(`#sidebarMenu .list-group-item[href="${activeLink}"]`).classList.add('active');
  }

  links.forEach(link => {
    link.addEventListener('click', function() {
      links.forEach(item => item.classList.remove('active'));
      this.classList.add('active');
      
      // Armazenar o estado 'active' no localStorage
      localStorage.setItem('activeLink', this.getAttribute('href'));
    });
  });
});