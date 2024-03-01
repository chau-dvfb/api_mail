// Xóa tất cả cookie hiện tại của m.kuku.lu và kuku.lu
document.cookie.split(";").forEach(function(cookie) { 
    let eqPos = cookie.indexOf("=");
    let name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=m.kuku.lu";
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=kuku.lu";
});

// Hỏi người dùng nhập chuỗi cookie
// let cookieString = prompt("Nhập chuỗi cookie:");

// if (!cookieString) {
//     alert("Vui lòng nhập một chuỗi cookie hợp lệ.");
// } else {
    cookieString = ""
    // Tách chuỗi cookie thành các cặp name và value
    let cookiePairs = cookieString.split(";").map(pair => pair.trim().split("="));

    // Thêm từng cookie vào trình duyệt
    cookiePairs.forEach(pair => {
        let name = pair[0];
        let value = pair[1];
        document.cookie = `${name}=${value}; path=/`;
    });

    // Reload trang web sau khi thêm cookie mới
    location.reload();
// }
