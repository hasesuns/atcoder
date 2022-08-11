use proconio::input;

fn main() {
    input! {
        (n, m, t): (i64, usize, i64),
        ab: [(i64, i64); m],
    }

    let mut battery = n;
    let mut now_time: i64 = 0;
    for (a, b) in &ab {
        battery -= a - now_time;
        if battery <= 0 {
            println!("No");
            return;
        }
        battery += b - a;
        battery = std::cmp::min(battery, n);
        now_time = *b;
    }
    battery -= t - now_time;
    if battery <= 0 {
        println!("No");
    } else {
        println!("Yes");
    }
}