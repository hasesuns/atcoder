use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: Chars
    }
    let mut max_len = 0;
    let k = n.len();
    for bit in 0..(1 << k) {
        let mut tmp_sum = 0;
        let sub_list = (0..k)
            .filter(|x| (bit & (1 << x)) != 0)
            .map(|x| n[x as usize])
            .collect::<Vec<_>>();
        for x in &sub_list {
            tmp_sum += *x as i32;
        }
        if tmp_sum % 3 == 0 && sub_list.len() > max_len {
            max_len = sub_list.len()
        }
    }

    if max_len != 0 {
        let ans = k - max_len;
        println!("{}", ans);
    } else {
        println!("-1")
    }
}