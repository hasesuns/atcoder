use proconio::input;

fn main() {
    input! {
        h: i32,
        w: i32,
        a: [[i32; w]; h],
    }
    let mut min = std::i32::MAX;
    let mut sum: i32 = 0;
    for a_h in a {
        for a_hw in a_h {
            if min > a_hw {
                min = a_hw
            }
            sum += a_hw
        }
    }
    let ans: i32 = sum - min * h * w;
    println!("{}", ans)
}