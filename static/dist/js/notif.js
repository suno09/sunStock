function notif(type, message) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
    });

    switch (type) {
        case 'success':
            toastr.success(message);
            break;
        case 'info':
            toastr.info(message);
            break;
        case 'error':
            toastr.error(message);
            break;
        case 'warning':
            toastr.warning(message);
            break;
    }
}
