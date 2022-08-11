use proconio::input;

fn main() {
    input! {
        nc: (usize, i64),
        abc: [(i64, i64, i64); nc.0]
    }
    let mut event_list: Vec<(i64, i64)> = vec![];
    abc.iter().for_each(|val| {
        event_list.push((val.0 - 1, val.2));
        event_list.push((val.1, -val.2));
    });

    event_list.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    let mut ans: i64 = 0;
    let mut now_pay: i64 = 0;
    let mut now_day: i64 = 0;
    for (day, pay) in event_list {
        if day != now_day {
            ans += (day - now_day) * std::cmp::min(nc.1, now_pay);
            now_day = day
        }
        now_pay += pay;
    }
    println!("{:?}", ans);
}