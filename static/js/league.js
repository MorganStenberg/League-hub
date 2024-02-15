const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const editErrorModal = new bootstrap.Modal(document.getElementById("editErrorModal"));
const deleteErrorModal = new bootstrap.Modal(document.getElementById("deleteErrorModal"));
const addMatchesErrorModal = new bootstrap.Modal(document.getElementById("addMatchesErrorModal"))
const editButtons = document.getElementsByClassName("btn-edit-error");
const deleteErrorButtons = document.getElementsByClassName("btn-delete-error");
const addMatchesErrorButtons= document.getElementsByClassName("btn-add-match-error")
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let matchId = e.target.getAttribute("data-match_id");
      deleteConfirm.href = `delete_match/${matchId}`;
      deleteModal.show();
    });
  }

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    editErrorModal.show();
  });
}

for (let button of deleteErrorButtons) {
  button.addEventListener("click", (e) => {
    deleteErrorModal.show();
  });
}


for (let button of addMatchesErrorButtons) {
  button.addEventListener("click", (e) => {
    addMatchesErrorModal.show();
  });
}
