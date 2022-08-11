use proconio::input;

fn main() {
    input! {
        (n, w): (usize, i64),
        stp: [(usize, usize, i64); n]
    }
    let t_max = 2 * 100_000;
    let mut imos_list: Vec<i64> = vec![Default::default(); t_max + 1];

    for (s, t, p) in stp {
        imos_list[s] += p;
        imos_list[t] -= p;
    }
    for i in 1..=t_max {
        imos_list[i] += imos_list[i - 1];
    }

    let max_sum = imos_list.iter().max().unwrap();
    if max_sum <= &w {
        println!("Yes");
    } else {
        println!("No");
    }
}