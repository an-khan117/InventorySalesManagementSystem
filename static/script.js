
const searchInput = document.getElementById("searchInput");
const productTable = document.getElementById("productTable");

searchInput.addEventListener("input", function () {
    const searchTerm = this.value.toLowerCase().trim();
    const rows = productTable.querySelectorAll("tbody tr");

    rows.forEach(function (row) {
        const rowText = row.textContent.toLowerCase();
        row.style.display = rowText.includes(searchTerm) ? "" : "none";
    });
});
