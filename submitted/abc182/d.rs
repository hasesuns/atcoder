use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }
    let mut ans: i64 = 0;
    let mut acc_list = vec![0];
    let mut instant_max_list = vec![0];

    let mut acc = 0;
    for i in 1..=n {
        acc += a[i-1];
        acc_list.push(acc);
        instant_max_list.push(std::cmp::max(acc, instant_max_list[i-1]));
    }

    let mut now: i64 = 0;
    for i in 0..=n {
        ans = std::cmp::max(ans, now + instant_max_list[i]);
        now += acc_list[i];
    }

    println!("{}", ans);
}