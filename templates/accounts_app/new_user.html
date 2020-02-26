<!-- new user modal -->
<div class="modal fade" id="modal-new-user">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title">Nouveau Utilisateur</h4>
        <button type="button" class="close" data-dismiss="modal" aria-label="Non">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="#" method="POST" id="form-new-user">
          <div class="form-group row">
            <label for="inputNewUsername" class="col-sm-3 col-form-label">Username</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" placeholder="Username" id="new-username" name="username" required autofocus>
            </div>
          </div>
          <div class="form-group row">
            <label for="inputNewPassword" class="col-sm-3 col-form-label">Mot de passe</label>
            <div class="col-sm-9">
              <input type="password" class="form-control" id="new-password" placeholder="Mot de passe" name="password" required>
            </div>
          </div>
          <div class="form-group row">
            <label for="inputTypeUser" class="col-sm-3 col-form-label">Role</label>
            <div class="col-sm-9">
              <select class="form-control" name="role" id="new-role">
                <option value="1">ADMIN</option>
                <option value="2">GERANT</option>
                <option value="3">VENDEUR</option>
              </select>
            </div>
          </div>
      </div>
      <div class="modal-footer justify-content-between">
        <button type="submit" class="btn btn-primary">Valider</button>
        <button type="reset" class="btn btn-default" data-dismiss="modal">Annuler</button>
      </div>
      </form>
    </div>
    <!-- /.modal-content -->
  </div>
  <!-- /.modal-dialog -->
</div>

<!-- jQuery -->
<script src="plugins/jquery/jquery.min.js"></script>

<script>
  function new_user() {
    var a = document.createElement("a");
    a.href = "#";
    var clickEvent = new MouseEvent("click", {
      "view": window,
      "bubbles": true,
      "cancelable": false
    });
    a.dispatchEvent(clickEvent);
  }

  $('#form-new-user').submit(function(event) {
    event.preventDefault();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=insert&" + $('#form-new-user').serialize(),
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (jresponse.type == 1) {
          notif('success', jresponse.message);
          setTimeout(function(){ window.location.reload(false); }, 1000);
        } else {
          notif('error', jresponse.message);
        }
      },
      error: function() {},
    });
  });

  function init_form_new_user() {
    $('#form-new-user')[0].reset();
    $("#modal-new-user").modal("show")
    return false;
  }
</script>