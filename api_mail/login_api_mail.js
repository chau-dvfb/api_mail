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
    cookieString = "cf_clearance=lLFTT_rvQ.PtKoC1a6qkrsVhSRCCF6lVelOBGlJbjGE-1708868542-1.0-AYAfyxJvrb+V/vor2uCLb/opDz9B1FUIo3NJfu8uJtxVh82RjUrHcxUVDyizv1LU2wbS1rBjdgGFUQcxbJCJroM=; cookie_csrf_token=ef3befb611fc1781b0ed3eac7d7a54c1; cookie_sessionhash=SHASH%3A5a7325a03fc42bc520e272e6f0470fdf; cookie_keepalive_insert=1; _ga=GA1.1.1799045359.1708868553; cookie_failedSlot=; cookie_timezone=Asia%2FBangkok; __gads=ID=e5bf7a70b51de553:T=1708868553:RT=1708868553:S=ALNI_MYxyRToikdnY7836dlXTgURTuZDOw; __gpi=UID=00000d14fd7c8e25:T=1708868553:RT=1708868553:S=ALNI_MbJcAzSCtjIBRevItV75wuTSZfX0Q; __eoi=ID=2694c82389cced96:T=1708868553:RT=1708868553:S=AA-Afjb_E-YIemUd_VNKsrkznfmx; cookie_gendomainorder=fanclub.pm; _ga_HMG13DJCGJ=GS1.1.1708868552.1.1.1708868707.0.0.0; cookie_last_page_recv=0; cookie_sessionhash=SHASH%3A5a7325a03fc42bc520e272e6f0470fdf; _ga=GA1.1.1799045359.1708868553; cookie_failedSlot=; cookie_timezone=Asia%2FBangkok; cookie_last_page_addrlist=0; cookie_last_page_recv=0; cookie_last_page_send=0; cookie_filter_mailaddr=; cookie_filter_mailtype=; cookie_filter_mailfilter=; cookie_filter_recv2=; _ga_HMG13DJCGJ=GS1.1.1708953006.2.1.1708954071.0.0.0; __gads=ID=e5bf7a70b51de553:T=1708868553:RT=1708954072:S=ALNI_MYxyRToikdnY7836dlXTgURTuZDOw; __gpi=UID=00000d14fd7c8e25:T=1708868553:RT=1708954072:S=ALNI_MbJcAzSCtjIBRevItV75wuTSZfX0Q; __eoi=ID=2694c82389cced96:T=1708868553:RT=1708954072:S=AA-Afjb_E-YIemUd_VNKsrkznfmx"
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
